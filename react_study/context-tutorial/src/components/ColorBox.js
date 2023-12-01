// import { ColorConsumer } from "../contexts/color";
import { useContext } from "react";
import ColorContext from "../contexts/color";

const ColorBox = () => {
  const { state } = useContext(ColorContext);
  return (
    <>
      <div
        style={{
          width: "64px",
          height: "64px",
          background: state.color,
        }}
      />
      <div
        style={{
          width: "32px",
          height: "32px",
          background: state.subcolor,
        }}
      />
    </>
  );
};

export default ColorBox;

// const ColorBox = () => {
//   return (
//     <ColorConsumer>
//       {({ state }) => (
//         <>
//           <div
//             style={{
//               width: "64px",
//               height: "64px",
//               background: state.color,
//             }}
//           />
//           <div
//             style={{
//               width: "32px",
//               height: "32px",
//               background: state.subcolor,
//             }}
//           />
//         </>
//       )}
//     </ColorConsumer>
//   );
// };

// export default ColorBox;

// const ColorBox = () => {
//   return (
//     <ColorConsumer>
//       {(value) => (
//         <>
//           <div
//             style={{
//               width: "64px",
//               height: "64px",
//               background: value.state.color,
//             }}
//           />
//           <div
//             style={{
//               width: "32px",
//               height: "32px",
//               background: value.state.subcolor,
//             }}
//           />
//         </>
//       )}
//     </ColorConsumer>
//   );
// };

// export default ColorBox;

// import ColorContext from "../contexts/color";

// const ColorBox = () => {
//   return (
//     <ColorContext.Consumer>
//       {(value) => (
//         <div
//           style={{
//             width: "64px",
//             height: "64px",
//             background: value.color,
//           }}
//         />
//       )}
//     </ColorContext.Consumer>
//   );
// };

// export default ColorBox;
