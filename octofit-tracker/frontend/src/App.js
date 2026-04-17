

import octofitLogo from '../public/octofitapp-small.png';


function App() {
  return (
    <div className="container py-4">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary rounded mb-4">
        <NavLink className="navbar-brand d-flex align-items-center" to="/">
          <img src={octofitLogo} alt="Octofit Logo" className="octofit-logo me-2" />
          <span className="fw-bold text-white">Octofit Tracker</span>
        </NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link text-white" to="/activities">Activities</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link text-white" to="/leaderboard">Leaderboard</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link text-white" to="/teams">Teams</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link text-white" to="/users">Users</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link text-white" to="/workouts">Workouts</NavLink>
            </li>
          </ul>
        </div>
      </nav>
      <div className="mb-4">
        <h1 className="display-4 text-center fw-bold">Octofit Tracker</h1>
      </div>
      <Routes>
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/users" element={<Users />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/" element={<div className="text-center"><h2 className="fw-bold">Welcome to Octofit Tracker!</h2><p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p></div>} />
      </Routes>
    </div>
  );
}

export default App;
