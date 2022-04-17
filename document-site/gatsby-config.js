
module.exports = {
  siteMetadata: {
    title: `���ϸ��� ���ݾ�`,
    name: `������ �����`,
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
      forcedNavOrder: ["/About Me", "/SW��ũ", "/����", "/������ �м�", "/����ö��"],
      ignoreIndex: true
    }
  },
  
  plugins: [{ resolve: `gatsby-theme-document` }]
};
