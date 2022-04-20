content_main_config = """

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
    { resolve: `gatsby-theme-document` }
  ]
};
"""

content_sub_config = """
// import { useColorMode } from '../theme-ui'
// const [colorMode, setColorMode] = useColorMode()

// if (colorMode=='dark') {


if ( true ) {
  color1 = "gray";
} else {
  color1 = "white";
}

module.exports = {
  siteMetadata: {
    title: `Document by Code Bushi`,
    name: `Code Bushi`,
    siteUrl: `https://codebushi.com`,
    description: `This is my description that will be used in the meta tags and important for search results`,
    social: [
      {
        name: `github`,
        url: `https://github.com/codebushi`
      },
      {
        name: `twitter`,
        url: `https://twitter.com/HuntaroSan`
      }
    ],
    sidebarConfig: {
      forcedNavOrder: ['/'],
      ignoreIndex: false
    }
  },
  plugins: [
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        path: `content`,
        name: `content`
      }
    },
    {
      resolve: `gatsby-plugin-mdx`,
      options: {
        extensions: [`.mdx`, `.md`],
        gatsbyRemarkPlugins: [
          {
            resolve: `gatsby-remark-images`,
            options: {
              maxWidth: 704
            }
          },
          {
            resolve: `gatsby-remark-autolink-headers`,
            options: {
              icon: false
            }
          },
          `gatsby-remark-embed-video`
        ]
      }
    },
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `Document`,
        short_name: `Document`,
        start_url: `/`,
        background_color: `#182952`,
        theme_color: `#a2466c`,
        display: `standalone`,
        icon: 'src/site-icon.png'
      }
    },
    `gatsby-plugin-sharp`,
    `gatsby-plugin-emotion`,
    `gatsby-plugin-theme-ui`,
    `gatsby-plugin-react-helmet`
    ,
    {
      resolve: `gatsby-plugin-scroll-indicator`,
      options: {
        // Configure color of the scroll indicator
        // color: "gray",
        color: color1,
        // color: ${p => p.theme.colors.text},
        // Height of the scroll indicator
        height: "6px",
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
    f.write(content_main_config)

with open("node_modules/gatsby-theme-document/gatsby-config.js", "w") as f:
    f.write(content_sub_config)