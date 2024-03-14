import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Nav from "./components/navigation/Nav"
import HomePage from "./pages/HomePage"
import Dashboard from "./pages/Dashboard"
import LoginPage from "./pages/LoginPage"
import RegisterPage from "./pages/RegisterPage"
import ResetPasswordPage from "./pages/ResetPasswordPage"
import ResetPasswordPageConfirm from "./pages/ResetPasswordPageConfirm";
import ActivatePage from "./pages/ActivatePage";
import NotFoundPage from "./pages/NotFoundPage";
import CreateTeamPage from "./pages/CreateTeamPage";
import UpdateProfilePage from "./pages/UpdateProfilePage";
import EditTeamPage from "./pages/EditTeamPage";
import DivisionsPage from "./pages/DivisionsPage";
import DivisionDetailsPage from "./pages/DivisionDetails";
import TeamPage from "./pages/TeamsPage";
import TeamDetailsPage from "./pages/TeamDetails";

function App() {
  return (
    <>
      <Router>
        <Nav />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/activate/:uid/:token" element={<ActivatePage />} />
          <Route path="/reset-password" element={<ResetPasswordPage />} />
          <Route path="/password/reset/confirm/:uid/:token" element={<ResetPasswordPageConfirm />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="*" element={<NotFoundPage />} />
          <Route path="/createteam" element={<CreateTeamPage />} />
          <Route path="/editteam" element={<EditTeamPage />} />
          <Route path="/myprofile" element={<UpdateProfilePage />} />
          <Route path="/divisions" element={<DivisionsPage />} />
          <Route path="/division/:name" element={<DivisionDetailsPage />} />
          <Route path="/allteams" element={<TeamPage />} />
          <Route path="/team/:id" element={<TeamDetailsPage />} />

        </Routes>
      </Router>
      <ToastContainer />
    </>
  )
}

export default App
