def set_contents(left_side_bar_width):
    content_for_NavItem = """import styled from '@emotion/styled';
import { Link } from 'gatsby';
import React, { useContext } from 'react';
import { GlobalDispatchContext, GlobalStateContext } from '../../context/GlobalContextProvider';
import ButtonCollapse from '../ButtonCollapse';

const NavItem = ({ item }) => {
const state = useContext(GlobalStateContext);
const dispatch = useContext(GlobalDispatchContext);
const isCollapsed = state.collapsed[item.url];
const hasChildren = item.items && item.items.length > 0;
return (
    <StyledNavItem>
    <NavItemLink to={item.url} activeClassName="is-active">
        {item.title}
    </NavItemLink>
    {hasChildren && (
        <ButtonCollapse
        onClick={() => {
            dispatch({ type: 'TOGGLE_NAV_COLLAPSED', url: item.url });
        }}
        isCollapsed={isCollapsed}
        />
    )}
    {hasChildren && isCollapsed && (
        <NavItemChild>
        {item.items.map(child => (
            <StyledNavItem key={child.url}>
            <NavItemLink to={child.url} activeClassName="is-active">
                {child.title}
            </NavItemLink>
            </StyledNavItem>
        ))}
        </NavItemChild>
    )}
    </StyledNavItem>
);
};

const StyledNavItem = styled.li`
position: relative;
display: block;
padding: 0;
margin: 0.2rem 0;
width: 100%;
list-style: none;
`;

const NavItemLink = styled(Link)`
display: block;
padding: 0.5rem 1.8rem 0.5rem 1.2rem;
width: 100%;
color: ${p => p.theme.colors.text};
font-weight: 600;
text-decoration: none;
transition: color ${p => p.theme.transition};
&:hover,
&:focus,
&.is-active {
    color: ${p => p.theme.colors.primary};
}
`;

const NavItemChild = styled.ul`
margin: 0.5rem 0 0.5rem 1.2rem;
padding: 0;
border-left: 1px solid ${p => p.theme.colors.text};
list-style: none;
& > li {
    margin: 0;
}
`;
export default React.memo(NavItem);"""

    content_for_ButtonCollapse = """
import styled from '@emotion/styled';
import PropTypes from 'prop-types';
import React from 'react';
import Add from './icons/Add';
import Icon from './icons/Icon';
import Minimize from './icons/Minimize';

const ButtonCollapse = ({ onClick, isCollapsed }) => {
  return (
    <StyledButtonCollapse
      onClick={onClick}
      aria-label="Toggle Subnavigation"
      title="Toggle Subnavigation"
    >
    {
        isCollapsed ? <Icon icon={<Minimize />} size={24} /> : <Icon icon={<Add />} size={24} />
        //isCollapsed ? <Icon icon={<Add />} size={24} /> : <Icon icon={<Minimize />} size={24} />
    }
    </StyledButtonCollapse>
  );
};

const StyledButtonCollapse = styled.button`
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.8rem;
  height: 37px;
  background: none;
  border: 0;
  color: ${p => p.theme.colors.text};
  cursor: pointer;
  font-size: 1rem;
`;

ButtonCollapse.propTypes = {
  onClick: PropTypes.func.isRequired,
  isCollapsed: PropTypes.bool
};

export default ButtonCollapse;"""
    content_for_LeftSidebar_index = f"""
import styled from '@emotion/styled';
import PropTypes from 'prop-types';
import React from 'react';
import mediaqueries from '../../styles/media';
import Navigation from './Navigation';

const LeftSidebar = ({{ navOpen }}) => {{
  return (
    <LeftSidebarWrapper>
      <LeftSidebarNav navOpen={{navOpen}}>
        <Navigation />
      </LeftSidebarNav>
    </LeftSidebarWrapper>
  );
}};

const LeftSidebarWrapper = styled.aside`
  margin-left: -{left_side_bar_width}rem;
  flex: 0 0 {left_side_bar_width}rem;
  font-size: 0.875rem;
  ${{mediaqueries.desktop_up`
    margin-left: 0;
  `}};
`;

const LeftSidebarNav = styled.nav`
  position: fixed;
  top: 0;
  bottom: 0;
  overflow-x: hidden;
  overflow-y: auto;
  width: {left_side_bar_width}rem;
  height: 100%;
  padding: 1rem 0;
  background: ${{p => p.theme.colors.sidebar}};
  transition: 0.25s var(--ease-in-out-quad);
  transform: ${{p => (p.navOpen ? `translateX({left_side_bar_width}rem)` : null)}};
  ${{mediaqueries.desktop_up`
    transform: translateX(0);
    padding: 6.6rem 0 1rem;
  `}};
`;

LeftSidebar.propTypes = {{
  navOpen: PropTypes.bool
}};

export default React.memo(LeftSidebar);
"""
    content_for_Header = f"""
import styled from '@emotion/styled';
import PropTypes from 'prop-types';
import React from 'react';
import useCycleColor from '../hooks/useCycleColor';
import mediaqueries from '../styles/media';
import ColorToggle from './icons/ColorToggle';
import IconButton from './icons/IconButton';
import Menu from './icons/Menu';
import LogoWrapper from './LogoWrapper';
import SocialIcons from './SocialIcons';

const Header = ({{ navOpen, setNavOpen }}) => {{
  const {{ cycleColorMode }} = useCycleColor();
  return (
    <StyledHeader navOpen={{navOpen}}>
      <HeaderSection>
        <NavIconButton>
          <IconButton
            label="Open Navigation"
            icon={{<Menu />}}
            size={{30}}
            onClick={{() => {{
              setNavOpen(!navOpen);
            }}}}
          />
        </NavIconButton>
        <LogoWrapper />
      </HeaderSection>
      <HeaderSection>
        <SocialIcons />
        <IconButton
          label="Change Theme Color"
          icon={{<ColorToggle />}}
          size={{30}}
          onClick={{cycleColorMode}}
        />
      </HeaderSection>
    </StyledHeader>
  );
}};

const StyledHeader = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1rem;
  z-index: 5;
  background: ${{p => p.theme.colors.background}};
  transition: all 0.25s var(--ease-in-out-quad);
  border-bottom: 1px solid ${{p => p.theme.colors.borderColor}};
  transform: ${{p => (p.navOpen ? `translateX({left_side_bar_width}rem)` : null)}};
  ${{mediaqueries.desktop_up`
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    padding: 1rem 1.2rem;
    transform: translateX(0);

  `}};
`;

const NavIconButton = styled.div`
  display: flex;
  margin-right: 1rem;
  ${{mediaqueries.desktop_up`
    display: none;
  `}};
`;

const HeaderSection = styled.div`
  display: flex;
  align-items: center;
`;

Header.propTypes = {{
  navOpen: PropTypes.bool,
  setNavOpen: PropTypes.func
}};

export default Header;

"""
    content_for_Layout = f"""
import {{ Global }} from '@emotion/core';
import styled from '@emotion/styled';
import PropTypes from 'prop-types';
import React, {{ useState }} from 'react';
import {{ Styled }} from 'theme-ui';
import {{ globalStyles }} from '../styles';
import mediaqueries from '../styles/media';
import Header from './Header';
import LeftSidebar from './LeftSidebar';
import RightSidebar from './RightSidebar';

const Layout = ({{ children, tableOfContents, location }}) => {{
  const [navOpen, setNavOpen] = useState(false);
  return (
    <Styled.root>
      <Global styles={{globalStyles}} />
      <Header navOpen={{navOpen}} setNavOpen={{setNavOpen}} />
      <SiteWrapper>
        <LeftSidebar navOpen={{navOpen}} />
        <SiteContentWrapper>
          <SiteContent navOpen={{navOpen}}>{{children}}</SiteContent>
        </SiteContentWrapper>
        {{tableOfContents.items && (
          <RightSidebar tableOfContents={{tableOfContents}} location={{location}} />
        )}}
      </SiteWrapper>
    </Styled.root>
  );
}};

const SiteWrapper = styled.div`
  display: flex;
  min-height: 100vh;
  overflow-x: hidden;
  background: ${{p => p.theme.colors.background}};
  transition: background 0.25s var(--ease-in-out-quad);
`;

const SiteContentWrapper = styled.div`
  flex-grow: 1;
  min-width: 20rem;
`;

const SiteContent = styled.main`
  padding: 2rem 1rem 2rem;
  transition: 0.25s var(--ease-in-out-quad);
  opacity: ${{p => (p.navOpen ? 0.3 : 1)}};
  transform: ${{p => (p.navOpen ? `translateX({left_side_bar_width}rem)` : null)}};
  ${{mediaqueries.desktop_up`
    transform: translateX(0);
    opacity: 1;
    padding: 7rem 3rem 3rem;
    max-width: 50rem;
  `}};
`;

Layout.propTypes = {{
  children: PropTypes.node.isRequired,
  tableOfContents: PropTypes.object.isRequired,
  location: PropTypes.object.isRequired
}};

export default Layout;
"""
    return content_for_NavItem, content_for_ButtonCollapse, content_for_LeftSidebar_index, content_for_Header, content_for_Layout


if __name__=="__main__":
    content_for_NavItem, content_for_ButtonCollapse, content_for_LeftSidebar_index, content_for_Header, content_for_Layout = set_contents(left_side_bar_width=20)

    base_dir = "node_modules/gatsby-theme-document/src"
    with open(f"{base_dir}/components/LeftSidebar/NavItem.js", "w") as f:
        "좌측 네비게이션 바에서 목록의 펼침/닫음 조건을 뒤집음. isCollapsed 를 !isCollapsed로 변경"
        f.write(content_for_NavItem)

    with open(f"{base_dir}/components/ButtonCollapse.js", "w") as f:
        "+ - 모양 변경"
        f.write(content_for_ButtonCollapse)

    with open(f"{base_dir}/components/LeftSidebar/index.js", "w") as f:
        "좌측 Nav 폭 조정"
        f.write(content_for_LeftSidebar_index)

    with open(f"{base_dir}/components/Header.js", "w") as f:
        "브라우저의 폭이 좁을때 (좌측 Nav바 사라질때의 폭 조정"
        f.write(content_for_Header)

    with open(f"{base_dir}/components/Layout.js", "w") as f:
        "폭 조정을 위해 Layout.js 수정"
        f.write(content_for_Layout)