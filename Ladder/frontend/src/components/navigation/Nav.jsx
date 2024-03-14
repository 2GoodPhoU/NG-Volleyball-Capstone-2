import React from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { logout, reset } from '../../features/auth/authSlice'
import { toast } from 'react-toastify'

const Nav = () => {

    const navigate = useNavigate()
    const dispatch = useDispatch()

    const { user } = useSelector((state) => state.auth)

    const handleLogout = () => {
        dispatch(logout())
        dispatch(reset())
        navigate("/")
    }


    return (
        <nav className="navbar">
            <NavLink className="logo" to="/">Logo</NavLink>
            <ul className="nav-links">
                {user ?
                    <>
                        <NavLink className='nav-childs' to="/dashboard">Dashboard</NavLink>
                        <NavLink className='nav-childs' to="/createteam">Create Team</NavLink>
                        <NavLink className='nav-childs' to="/allteams"> Teams</NavLink>
                        <NavLink className='nav-childs' to="/myprofile">Profile</NavLink>
                        <NavLink className='nav-childs' to="/divisions">Divisions</NavLink>
                        <NavLink className='nav-childs' to="/" onClick={handleLogout}>Logout</NavLink>

                    </>
                    :
                    <>
                        <NavLink className='nav-childs' to="/divisions">Divisions</NavLink>
                    </>
                }
            </ul>
        </nav>
    )
}

export default Nav