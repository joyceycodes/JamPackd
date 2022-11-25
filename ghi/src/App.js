import { useEffect, useState } from 'react';

import './css/App.css';

function App() {


  return (
    <header>
    <p className="JP_title borderstyle">JamPack'd</p>
    <p className="JP_subtitle borderstyle">Pack'd Full of Tasty Jams!</p>
        <nav>
      <ul>
        <li>
          <button type="button" className="login-btn fbstyle">Login</button>
        </li>
        <li>
          <button type="button" className="signup-btn fbstyle">Sign Up</button>
        </li>
      </ul>
    </nav>
    </header>
    
  );
}

export default App;
