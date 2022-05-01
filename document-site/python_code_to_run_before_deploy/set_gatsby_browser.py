content_sub_browser = """
import React from 'react';
import GlobalContextProvider from './src/context/GlobalContextProvider';
import "katex/dist/katex.min.css";

export const wrapRootElement = ({ element }) => (
  <GlobalContextProvider>{element}</GlobalContextProvider>
);
"""

with open("node_modules/gatsby-theme-document/gatsby-browser.js", "w") as f:
    f.write(content_sub_browser)