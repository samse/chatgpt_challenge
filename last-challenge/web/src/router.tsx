import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import NotFound from "./common/NotFound";
import Header from "./routes/Header";
import Search from "./routes/Search";
import Home from "./routes/Home";

const router = createBrowserRouter(
    [{
    path: "/",
    element: <App />,
    children: [
        {
            path: "search/:keyword",
            element: <Search />
        },
        {
            path: "/",
            element: <Home />
        }
    ],
    errorElement: <NotFound />,
}
], {
basename: '/jobs'
}
);

export default router;