import ColorBox from "./components/ColorBox";
import { ColorProvider } from "./contexts/color";
import SelectColors from "./components/SelectColors";

const App = () => {
  return (
    <ColorProvider>
      <div>
        <SelectColors />
        <ColorBox />
      </div>
    </ColorProvider>
  );
};

// const App = () => {
//   return (
//     <ColorProvider>
//       <div>
//         <ColorBox />
//       </div>
//     </ColorProvider>
//   );
// };

// const App = () => {
//   return (
//     <div>
//       <ColorContext.Provider value={{ color: "red" }}>
//         <div>
//           <ColorBox />
//         </div>
//       </ColorContext.Provider>
//     </div>
//   );
// };

export default App;
