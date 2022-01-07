import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Root from './pages/index.js';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter} from "react-router-dom"


ReactDOM.render(
  // 브라우저 라우터(react-router-dom)로 root 를 감싸어 라우팅이 가능토록 
  <BrowserRouter>
    <Root/>
  </BrowserRouter>,
  document.getElementById('root')
);

reportWebVitals();
