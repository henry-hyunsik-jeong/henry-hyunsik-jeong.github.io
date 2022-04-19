content = """

module.exports = {
  siteMetadata: {
    title: `매일매일 조금씩`,
    name: `정현식`,
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
      forcedNavOrder: ["/About Me", "/개똥철학", "/SW테크", "/데이터 분석", "/금융"],
      ignoreIndex: true
    }
  },
  
  plugins: [
    { resolve: `gatsby-theme-document` },
    {
      resolve: `gatsby-plugin-scroll-indicator`,
      options: {
        // Configure color of the scroll indicator
        color: "white",
        // Height of the scroll indicator
        height: "3px",
        // Configure paths where the scroll indicator will appear
        paths: ["/"],
        // Configure the z-index of the indicator element
        zIndex: `9999`
      }
    }
  ]
};
"""
with open("gatsby-config.js", "w") as f:
    f.write(content)