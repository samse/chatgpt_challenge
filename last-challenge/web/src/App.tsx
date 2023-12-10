import React from 'react';
import './App.css';
import { ThemeProvider } from 'styled-components';
import { GlobalStyle } from './common/GlobalStyle';
import { Outlet } from 'react-router-dom';
import { darkTheme, lightTheme } from './theme/theme';
import { ReactQueryDevtools } from "react-query/devtools";
import { useRecoilValue, useSetRecoilState } from 'recoil';
import { DarkModeAtom } from './common/atoms';

function App() {
  const setDarkMode = useSetRecoilState(DarkModeAtom);
  const isDark = useRecoilValue(DarkModeAtom);

  return <>
      <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
        <GlobalStyle />
        <Outlet />
        <ReactQueryDevtools />
      </ThemeProvider>
</>;
}

export default App;
