import { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import { BiUser } from 'react-icons/bi';
import { useDispatch, useSelector } from 'react-redux';
import { register, reset } from '../features/auth/authSlice';
import { useNavigate } from 'react-router-dom';
import Spinner from '../components/Spinner';

const RegisterPage = () => {
    const [formData, setFormData] = useState({
        "first_name": "",
        "last_name": "",
        "username": "",
        "email": "",
        "password": "",
        "re_password": "",
        "profile_pic": null,
    });

    const { first_name, last_name, username, email, password, re_password, profile_pic } = formData;

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const { user, isLoading, isError, isSuccess, message } = useSelector((state) => state.auth);

    const handleChange = (e) => {
        setFormData((prev) => ({
            ...prev,
            [e.target.name]: e.target.value,
        }));
    };

    const handleFileChange = (e) => {
        setFormData((prev) => ({
            ...prev,
            [e.target.name]: e.target.files[0],
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (password !== re_password) {
            toast.error("Passwords do not match");
        } else {
            const userData = new FormData();
            userData.append("first_name", first_name);
            userData.append("last_name", last_name);
            userData.append("username", username);
            userData.append("email", email);
            userData.append("password", password);
            userData.append("re_password", re_password);
            userData.append("profile_pic", profile_pic);

            dispatch(register(userData));
        }
    };

    useEffect(() => {
        if (isError) {
            toast.error(message);
        }

        if (isSuccess || user) {
            navigate("/");
            toast.success("An activation email has been sent to your email. Please check your email");
        }

        dispatch(reset());
    }, [isError, isSuccess, user, navigate, dispatch]);

    return (
        <>
            <div className="container auth__container">
                <h1 className="main__title">Register <BiUser /> </h1>

                {isLoading && <Spinner />}

                <form className="auth__form">
                    <input
                        type="text"
                        placeholder="First Name"
                        name="first_name"
                        onChange={handleChange}
                        value={first_name}
                        required
                    />
                    <input
                        type="text"
                        placeholder="Last Name"
                        name="last_name"
                        onChange={handleChange}
                        value={last_name}
                        required
                    />
                    <input
                        type="text"
                        placeholder="Username"
                        name="username"
                        onChange={handleChange}
                        value={username}
                        required
                    />
                    <input
                        type="email"
                        placeholder="Email"
                        name="email"
                        onChange={handleChange}
                        value={email}
                        required
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        name="password"
                        onChange={handleChange}
                        value={password}
                        required
                    />
                    <input
                        type="password"
                        placeholder="Retype Password"
                        name="re_password"
                        onChange={handleChange}
                        value={re_password}
                        required
                    />
                    <input
                        type="file"
                        name="profile_pic"
                        accept="image/*"
                        onChange={handleFileChange}
                        required
                    />
                    <button className="btn btn-primary" type="submit" onClick={handleSubmit}>
                        Register
                    </button>
                </form>
            </div>
        </>
    );
};

export default RegisterPage;
