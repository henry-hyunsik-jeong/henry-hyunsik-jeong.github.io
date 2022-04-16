
base_dir = "node_modules/gatsby-theme-document/src"

def set_color_set():
    content = """
export default {
text: '#fff',
background: 'hsl(230,25%,18%)',
primary: 'hsl(260, 100%, 80%)',
secondary: 'hsl(290, 100%, 80%)',
sidebar: 'hsla(230, 20%, 0%, 20%)',
borderColor: 'rgba(255, 255, 255, 0.15)',
modes: {
    notdark: {
    text: '#000',
    background: '#fff',
    primary: '#e63b19',
    secondary: '#c70d3a',
    sidebar: '#eee',
    borderColor: 'rgba(0, 0, 0, 0.15)'
    }
}
// text: '#000',
// background: '#fff',
// primary: '#e63b19',
// secondary: '#c70d3a',
// sidebar: '#eee',
// borderColor: 'rgba(0, 0, 0, 0.15)',
// modes: {
//   dark: {
//     text: '#fff',
//     background: '#182952',
//     primary: '#f638dc',
//     secondary: '#ff7976',
//     sidebar: '#101d3c',
//     borderColor: 'rgba(255, 255, 255, 0.15)'
//   },
//   cool: {
//     text: '#fff',
//     background: '#05386b',
//     primary: '#5cdb95',
//     secondary: '#bef992',
//     sidebar: '#052e56',
//     borderColor: 'rgba(255, 255, 255, 0.15)'
//   },
//   deep: {
//     text: '#fff',
//     background: 'hsl(230,25%,18%)',
//     primary: 'hsl(260, 100%, 80%)',
//     secondary: 'hsl(290, 100%, 80%)',
//     sidebar: 'hsla(230, 20%, 0%, 20%)',
//     borderColor: 'rgba(255, 255, 255, 0.15)'
//   }
// }
};
    """
    with open("src/gatsby-plugin-theme-ui/colors.js", "w") as f:
        f.write(content)
    with open(f"{base_dir}/gatsby-plugin-theme-ui/colors.js", "w") as f:
        f.write(content)


def set_color_cycle():
    content = """
import { useColorMode } from 'theme-ui';
import colors from '../gatsby-plugin-theme-ui/colors';

const customColors = Object.keys(colors.modes);
const modes = [...customColors, 'dark'];

function useCycleColor() {
  const [colorMode, setColorMode] = useColorMode();

  const cycleColorMode = () => {
    const i = modes.indexOf(colorMode);
    const n = (i + 1) % modes.length;
    setColorMode(modes[n]);
  };

  return { cycleColorMode };
}

export default useCycleColor;
"""
    with open(f"{base_dir}/hooks/useCycleColor.js", "w") as f:
        f.write(content)

set_color_set()
set_color_cycle()