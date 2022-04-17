

"RightSidebar.js 수정"

content = """
import styled from '@emotion/styled';
import { Link } from 'gatsby';
import PropTypes from 'prop-types';
import React, { useState, useEffect, useRef } from 'react';
import mediaqueries from '../styles/media';
import ListItem from './ListItem';

const useHeadingsData = () => {
  const [nestedHeadings, setNestedHeadings] = useState([]);

  useEffect(() => {
    const headingElements = Array.from(
      document.querySelectorAll("h2, h3")
    );

    const newNestedHeadings = getNestedHeadings(headingElements);
    setNestedHeadings(newNestedHeadings);
  }, []);

  return { nestedHeadings };
};

const getNestedHeadings = (headingElements) => {
  const nestedHeadings = [];

  headingElements.forEach((heading, index) => {
    const { innerText: title, id } = heading;

    if (heading.nodeName === "H2") {
      nestedHeadings.push({ id, title, items: [] });
    } else if (heading.nodeName === "H3" && nestedHeadings.length > 0) {
      nestedHeadings[nestedHeadings.length - 1].items.push({
        id,
        title,
      });
    }
  });

  return nestedHeadings;
};
const useIntersectionObserver = (setActiveId) => {
  const headingElementsRef = useRef({});
  useEffect(() => {
    const callback = (headings) => {
      headingElementsRef.current = headings.reduce((map, headingElement) => {
        map[headingElement.target.id] = headingElement;
        return map;
      }, headingElementsRef.current);

      const visibleHeadings = [];
      Object.keys(headingElementsRef.current).forEach((key) => {
        const headingElement = headingElementsRef.current[key];
        if (headingElement.isIntersecting) visibleHeadings.push(headingElement);
      });

      const getIndexFromId = (id) =>
        headingElements.findIndex((heading) => heading.id === id);

      if (visibleHeadings.length === 1) {
        setActiveId(visibleHeadings[0].target.id);
      } else if (visibleHeadings.length > 1) {
        const sortedVisibleHeadings = visibleHeadings.sort(
          (a, b) => getIndexFromId(a.target.id) > getIndexFromId(b.target.id)
        );
        setActiveId(sortedVisibleHeadings[0].target.id);
      }
    };

    const observer = new IntersectionObserver(callback, {
      rootMargin: "0px 0px -40% 0px"
    });

    const headingElements = Array.from(document.querySelectorAll("h2, h3"));

    headingElements.forEach((element) => observer.observe(element));

    return () => observer.disconnect();
  }, [setActiveId]);
};

const Headings = ({ headings, activeId }) => (
  <RightSidebarList>
    {headings.map((heading) => (
      <li key={heading.id} className={heading.id === activeId ? "active" : ""}>
        <a
          href={`#${heading.id}`}
            onClick={(e) => {
              e.preventDefault();
              document.querySelector(`#${heading.id}`).scrollIntoView({
                behavior: "smooth"
              });
            }}
          
          >
          {heading.title}
        </a>
        {heading.items.length > 0 && (
          <RightSidebarList>
            {heading.items.map((child) => (
              <li key={child.id} className={child.id === activeId ? "active" : ""}>
                <a
                  href={`#${child.id}`}
                  onClick={(e) => {
                    e.preventDefault();
                    document.querySelector(`#${child.id}`).scrollIntoView({
                      behavior: "smooth"
                    });
                  }}
                  >
                    {child.title}
                </a>
              </li>
            ))}
          </RightSidebarList>
        )}
      </li>
    ))}
  </RightSidebarList>
);

const RightSidebar = ({ tableOfContents, location, headings }) => {
  const [activeId, setActiveId] = useState();
  const { nestedHeadings } = useHeadingsData();
  useIntersectionObserver(setActiveId);
  return (
    <RightSidebarWrapper>
      <RightSidebarNav>
        <RightSidebarTitle>Contents</RightSidebarTitle>
        {<Headings headings={nestedHeadings} activeId={activeId} />}
      </RightSidebarNav>
    </RightSidebarWrapper>
  );
};

const RightSidebarWrapper = styled.aside`
  display: none;
  flex: 0 0 20rem;
  font-size: 1rem;
  font-weight: 600;
  ${mediaqueries.desktop_medium_up`
    display: block
  `};
`;

const RightSidebarNav = styled.nav`
  position: fixed;
  top: 0;
  bottom: 0;
  overflow-x: hidden;
  overflow-y: auto;
  width: 20rem;
  height: 100%;
  padding: 7rem 1rem 0;
`;

const RightSidebarTitle = styled.p`
  margin-top: 0;
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: uppercase;
`;
export const gray5 = "#e0dddd";
const RightSidebarList = styled.ul`
  margin: 0;
  padding: 0;
  
  a {
    color: grey;
    text-decoration: none;
  }

  li.active > a {
    color: ${p => p.theme.colors.text};
    text-decoration: none;
    transition: color ${p => p.theme.transition};
  }

  li > a:hover {
    color: ${p => p.theme.colors.text};
  }
`;
// border-top: 1px solid ${gray5};
// :first-of-type {
//   border-top: none;
// }

// list-style: none;

  const RightSidebarListItem = styled.li`
  margin: 0.3rem 0;
  a {
    color: grey;
    text-decoration: none;
  }

  active > a {
    color: blue;
  }

  a:hover {
    color: blue;
  }
`;

const li_manual = styled.li`
  
  height: 60px;
  a {
    
    display: block;
    position: relative;
    height: 60px;
    line-height: 65px;
    font-size: 32px;
    font-weight: 500;
    padding: 0 0px;
    margin: 0 16px;
    text-decoration: none;
    color: black;
    
  }
  .active {
    color: white;
  }
`;
const a_manual = styled.a`
  color: grey;
  text-decoration: none;
`;



RightSidebar.propTypes = {
  tableOfContents: PropTypes.object.isRequired,
  location: PropTypes.object.isRequired
};

export default RightSidebar;
"""

with open("node_modules/gatsby-theme-document/src/components/RightSidebar.js", "w") as f:
    f.write(content)