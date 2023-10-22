import axios from 'axios';
import { useEffect, useState } from 'react';
import './App.css';
// import { ConfigProvider, Timeline } from 'antd';
import Timeline from 'antd/lib/timeline';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';

interface ObjectId {
  $oid: string;
}

interface Event {
  _id: ObjectId;
  type: string;
  createdAt: number;
  data: any;
}

function CodeSnippet({ language, code }: { language: string, code: string }) {
  if (code.trim() === "") {
    return (<></>);
  }

  return (
    <SyntaxHighlighter language={language} style={docco}>
      {code}
    </SyntaxHighlighter>
  );
}

function EventTimelineItem(event: Event) {
  const date = new Date(event.createdAt);
  const formattedDate = new Intl.DateTimeFormat(
    'pt-BR',
    {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    }
  ).format(date);

  console.log(event);
  return (
    <Timeline.Item key={event._id.$oid}>
      <b>{formattedDate}:</b> {event.type}
      <p>{event.data.document.fileName}</p>
      {event.data.contentChanges?.map((change: any) => {
            return (
              <CodeSnippet language={event.data.document.languageId} code={change.text} />
            );
          })
      }
      {event.type === "textDocument/inlineCompletionReceived"
        ?
        <div>
          <p><b>Prompt:</b> {event.data.prompt}</p>
          <b>Suggestions:</b>
          {event.data.completionItems.map((completionItem: any) => {
            return (<CodeSnippet language={event.data.document.languageId} code={completionItem.insertText} />)
          })}
        </div>
        : <></>
      }

      {event.type === "textDocument/suggestionAccepted"
        ?
        <div>
          <p><b>Prompt:</b> {event.data.prompt}</p>
          <b>Suggestions:</b>
          {event.data.suggestions?.map((suggestion: string) => {
            return (<CodeSnippet language={event.data.document.languageId} code={suggestion ? suggestion : ""} />)
          })}
        </div>
        : <></>
      }
    </Timeline.Item>
  );
}

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/v1/events').then((response) => {
      setEvents(response.data.map((event: Event) => EventTimelineItem(event)));
    }).catch(error => {
      console.log(error)
    })
  }, []);

  return (
    <div className="App">
      <div style={{ padding: "100px" }}>
        <h1 style={{ marginBottom: "2rem" }}>
          Events
        </h1>
        <Timeline children={events}></Timeline>
      </div>
    </div>
  );
}

export default App;
