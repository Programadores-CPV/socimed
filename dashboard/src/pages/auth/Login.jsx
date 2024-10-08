//?COMPONENTS
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
//? ICONS
import { RiAccountCircleLine, RiLockLine, RiEyeLine, RiEyeOffLine, RiLoader4Fill } from 'react-icons/ri';
//? HOOKS
import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
//? REDUX
import { useDispatch } from 'react-redux';
import { setUser, unSetUser } from '../../redux/reducers/UserSlicer';
import { notify } from '/src/api/scripts/notifications';
import { AxiosInstance } from '../../api/axios'
//? IMG
import LogoSM from '/src/assets/img/logo-sm-color.svg'

const Login = () => {
	// Dynamic states
	const [showPassword, setShowPassword] = useState(false);
	const [isLoading, setIsLoading] = useState(false);
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	//redux States and Hooks
	const dispatch = useDispatch();
	// const access = useSelector(accessTokenSelector);
	// const refresh = useSelector(refreshTokenSelector);

	const userRef = useRef();
	const passwordRef = useRef();
	const navigate = useNavigate();
	
	// useEffect(() => {
	// 	// valida que el token siga activo
	// 	axiosRequest.VERIFY(access, refresh, dispatch, setTokens, navigate);
	// }, [access, dispatch, navigate, refresh]);
	useEffect(() => {
		dispatch(unSetUser())
	}, [dispatch])

	const HandleSubmit = e => {
		//! conexión asíncrona con Axios para login
		e.preventDefault();
		setIsLoading(true)
		AxiosInstance.post('login/', {username, password})
			.then(response => {
				dispatch(setUser(response.data));
				navigate('/');
			})
			.catch(error => {
				if (!error?.response) {
					notify.ERROR('El servidor no responde, comunicarse al 2434')
				} else {
					notify.ERROR(error.response.data.error);
				}
				passwordRef.current.focus();
			})
			.finally(() => setIsLoading(false))
		
	};

	return (
		<>
			<div className='flex items-center justify-center min-h-screen p-4'>
				<div className='bg-gradient-to-b from-neutral-100 to-neutral-300 p-8 rounded-xl shadow-2xl w-auto lg:w-[450px]'>
					<img src={LogoSM} className='h-[250px] m-auto' />
					<h1 className='text-3xl text-center uppercase font-bold tracking-[5px] text-orangecpv-500 mb-5'>Iniciar Sesión</h1>
					<form className='p-10' onSubmit={HandleSubmit}>
						<div className='relative mb-4'>
							<TextField
								fullWidth
								autoComplete='off'
								id="user_id"
								placeholder='Usuario'
								ref={userRef}
								required
								value={username}
								onChange={e => setUsername(e.target.value)}
								InputProps={{
									startAdornment: (
										<InputAdornment position="start">
											<RiAccountCircleLine className='text-orangecpv-500 text-[25px]' />
										</InputAdornment>
									),
								}}
								variant="standard"
							/>
						</div>
						<div className='relative mb-8'>
							<TextField
								fullWidth
								type={showPassword ? 'text' : 'password'}
								autoComplete='off'
								id="pass_id"
								placeholder='Contraseña'
								ref={passwordRef}
								required
								value={password}
								onChange={e => setPassword(e.target.value)}
								InputProps={{
									startAdornment: (
										<InputAdornment position="start">
											<RiLockLine className='text-orangecpv-500 text-[25px]' />
										</InputAdornment>
									),
									endAdornment: (
										<InputAdornment position="end">
											{showPassword ? (
												<>
													<Tooltip title='Ocultar Contraseña' placement='right'>
														<div>
															<RiEyeOffLine
																onClick={() => setShowPassword(!showPassword)}
																className='text-orangecpv-500 text-[25px] hover:cursor-pointer'
															/>
														</div>
													</Tooltip>
												</>
											) : (
												<>
													<Tooltip title='Mostrar Contraseña' placement='right'>
														<div>
															<RiEyeLine
																onClick={() => setShowPassword(!showPassword)}
																className='text-orangecpv-500 text-[25px] hover:cursor-pointer'
															/>
														</div>
													</Tooltip>
												</>
											)}
										</InputAdornment>
									),
								}}
								variant="standard"
							/>
						</div>
						<div>
							<Button
								type='submit'
								color='primary'
								variant='contained'
								disabled={isLoading}
								size='large'
								className='w-full text-sm font-bold uppercase rounded-lg bg-gradient-to-l from-orangecpv-500 to-orangecpv-600 dark:from-orangecpv-500 dark:to-orangecpv-600 hover:bg-gradient-to-r text-default disabled:opacity-40 disabled:from-light-400 disabled:to-light-500'
							>
								{
									isLoading ? <RiLoader4Fill className='text-2xl text-center animate-spin' /> : "Ingresar"
								}
							</Button>
						</div>
					</form>
				</div>
			</div>
			<ToastContainer />
		</>
	);
};

export default Login;
