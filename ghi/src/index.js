import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

var MyClass = React.createClass({
  render: function() {
    return (
      let <div>
        <a href="#" style={className clr='#fffd00'}><span>highlighter yellow</span><i /></a>
        <a href="#" style={{--clr: '#00e9ff'}}><span>teal</span><i /></a>
        <a href="#" style={{--clr: '#b800ff'}}><span>neon purple</span><i /></a>
      </div>
    );
  }
});

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
