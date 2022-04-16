

"Tistory 아이콘 생성"
content = """
import React from 'react';
import SVG from './SVG';

const Tistory = () => (
  <SVG viewBox="0 0 14 14">
    <g><circle class="cls-1" cx="1.9945" cy="1.9945" r="1.9945"/><circle class="cls-1" cx="7" cy="1.9945" r="1.9945"/><circle class="cls-1" cx="7" cy="7" r="1.9945"/><circle class="cls-1" cx="7" cy="12.006" r="1.9945"/><circle class="cls-1" cx="12.006" cy="1.9945" r="1.9945"/></g>
  </SVG>
);

export default Tistory;
"""
with open("node_modules/gatsby-theme-document/src/components/icons/Tistory.js", "w") as f:
    f.write(content)


"Linked In 아이콘 생성"
content = """
import React from 'react';
import SVG from './SVG';

const Linkedin = () => (
    <SVG viewBox="0 0 380 380" width="24" height="24">
    <path
      fillRule="evenodd"
      
      d="M347.445,0H34.555C15.471,0,0,15.471,0,34.555v312.889C0,366.529,15.471,382,34.555,382h312.889
	C366.529,382,382,366.529,382,347.444V34.555C382,15.471,366.529,0,347.445,0z M118.207,329.844c0,5.554-4.502,10.056-10.056,10.056
	H65.345c-5.554,0-10.056-4.502-10.056-10.056V150.403c0-5.554,4.502-10.056,10.056-10.056h42.806
	c5.554,0,10.056,4.502,10.056,10.056V329.844z M86.748,123.432c-22.459,0-40.666-18.207-40.666-40.666S64.289,42.1,86.748,42.1
	s40.666,18.207,40.666,40.666S109.208,123.432,86.748,123.432z M341.91,330.654c0,5.106-4.14,9.246-9.246,9.246H286.73
	c-5.106,0-9.246-4.14-9.246-9.246v-84.168c0-12.556,3.683-55.021-32.813-55.021c-28.309,0-34.051,29.066-35.204,42.11v97.079
	c0,5.106-4.139,9.246-9.246,9.246h-44.426c-5.106,0-9.246-4.14-9.246-9.246V149.593c0-5.106,4.14-9.246,9.246-9.246h44.426
	c5.106,0,9.246,4.14,9.246,9.246v15.655c10.497-15.753,26.097-27.912,59.312-27.912c73.552,0,73.131,68.716,73.131,106.472
	L341.91,330.654L341.91,330.654z"
    />
  </SVG>
  

);

export default Linkedin;
"""
with open("node_modules/gatsby-theme-document/src/components/icons/Linkedin.js", "w") as f:
    f.write(content)


import time
time.sleep(3)
"색인에 추가"
content = """
import styled from '@emotion/styled';
import { graphql, useStaticQuery } from 'gatsby';
import React from 'react';
import Github from './icons/Github';
import Icon from './icons/Icon';
import Twitter from './icons/Twitter';
import Tistory from './icons/Tistory';
import Linkedin from './icons/Linkedin';

const socialQuery = graphql`
  {
    allSite {
      edges {
        node {
          siteMetadata {
            social {
              name
              url
            }
          }
        }
      }
    }
  }
`;

const icons = {
  github: <Github />,
  twitter: <Twitter />,
  tistory: <Tistory />,
  linkedin: <Linkedin />
};

const SocialIcons = () => {
  const result = useStaticQuery(socialQuery);
  const socialOptions = result.allSite.edges[0].node.siteMetadata.social;
  return (
    <StyledSocialIcons>
      {socialOptions.map(option => (
        <SocialLinks key={option.name} href={option.url}>
          <Icon icon={icons[option.name]} size={22} />
        </SocialLinks>
      ))}
    </StyledSocialIcons>
  );
};

const StyledSocialIcons = styled.div`
  display: flex;
  align-items: center;
  margin-right: 2rem;
  opacity: 0.7;
`;

const SocialLinks = styled.a`
  display: inline-block;
  margin: 0 0.5rem;
`;

export default SocialIcons;
"""

with open("node_modules/gatsby-theme-document/src/components/SocialIcons.js", "w") as f:
    f.write(content)


"config에 반영"
content = """
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

"""

with open("gatsby-config.js", "w") as f:
  f.write(content)