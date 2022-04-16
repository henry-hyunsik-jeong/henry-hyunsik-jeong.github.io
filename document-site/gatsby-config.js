
module.exports = {
  siteMetadata: {
    title: `매일매일 조금씩`,
    name: `정현식 저장소`,
    siteUrl: `http://henryjeong.com`,
    description: `This is my description that will be used in the meta tags and important for search results`,
    social: [
      {
        name: `github`,
        url: `https://github.com/henry-hyunsik-jeong/henry-hyunsik-jeong.github.io`
      },
      {
        name: `tistory`,
        url: `https://henry-hyunsik-jeong.tistory.com/`
      },
      {
        name: `linkedin`,
        url: `https://www.linkedin.com/in/hyunsik/`
      }
    ],
    sidebarConfig: {
      forcedNavOrder: ["/About Me", "/SW테크", "/금융", "/데이터 분석", "/개똥철학"],
      ignoreIndex: true
    }
  },
  
  plugins: [{ resolve: `gatsby-theme-document` }]
};

