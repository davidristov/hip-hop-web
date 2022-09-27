import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import TopMenu from "./components/Nav/TopMenu";
import Artists from "./components/Artists/Artists";
import Records from "./components/Records/Records";

function App() {
  return (
    <>
      <Router>
        <TopMenu />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/Artists" element={<Artists />} />
          <Route path="/Records" element={<Records />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
