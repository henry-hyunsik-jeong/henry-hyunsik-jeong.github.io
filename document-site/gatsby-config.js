module.exports = {
  siteMetadata: {
    title: `정현식 저장소`,
    name: `Code Bushi`,
    siteUrl: `https://gatsby-theme-document.netlify.com`,
    description: `This is my description that will be used in the meta tags and important for search results`,
    social: [
      {
        name: `github`,
        url: `https://github.com/henry-hyunsik-jeong/henry-hyunsik-jeong.github.io`
      },
      // {
      //   name: `linkedin`,
      //   url: `https://github.com/henry-hyunsik-jeong/henry-hyunsik-jeong.github.io`
      // }
      // {
      //   name: `twitter`,
      //   url: `https://twitter.com/HuntaroSan`
      // }
    ],
    sidebarConfig: {
      forcedNavOrder: ["/introduction", "/codeblock", "/codeblock2"],
      ignoreIndex: true
    }
  },
  
  plugins: [{ resolve: `gatsby-theme-document` }]
};
