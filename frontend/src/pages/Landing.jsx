import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div>
      <Link to="/todo">
        <button className="btn">Todo list</button>
      </Link>
    </div>
  );
}
