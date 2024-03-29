'use client';

import Link from "next/link";
import {useAppDispatch, useAppSelector} from '@/redux/hooks';
import {useLogoutMutation} from '@/redux/features/authApiSlice';
import {logout as setLogout} from '@/redux/features/authSlice';

export default function Header() {
	const dispatch = useAppDispatch();
	const [logout] = useLogoutMutation();

	const {isAuthenticated} = useAppSelector(state => state.auth);

	const handleLogout = () => {
		logout(undefined)
			.unwrap()
			.then(() => {
				dispatch(setLogout());
			});
	};


	return (
		<>
			<header className="bg-white shadow-gray-800/50 shadow-sm ">
				<nav className="max-w-screen-xl px-6 sm:px-8 lg:px-16 mx-auto grid grid-flow-col py-3 sm:py-4 ">
					<div className="col-start-1 col-end-2 flex items-center">
						<Link href={"/"}>
							<h5 className="text-large font-bold">DIGITAL FORTRESS</h5>
						</Link>
					</div>
					<ul className="hidden lg:flex col-start-4 col-end-8 text-black-500  items-center">
						<Link
							href={"/"}
							className={
								"px-4 py-2 mx-2 cursor-pointer animation-hover inline-block relative hover:bg-gray-200 hover:bg-opacity-25"}
						>
							About
						</Link>
						<Link
							href={"/subscription"}
							className={
								"px-4 py-2 mx-2 cursor-pointer animation-hover inline-block relative hover:bg-gray-200 hover:bg-opacity-25"}
						>
							Subscription
						</Link>
						{isAuthenticated ? (
						<Link
							href={"/projects"}
							className={
								"px-4 py-2 mx-2 cursor-pointer animation-hover inline-block relative hover:bg-gray-200 hover:bg-opacity-25"
							}
						>
							Projects
						</Link>
						): null}

					</ul>

					{isAuthenticated ? (
						<>
							<div className="col-start-10 col-end-12 font-medium flex justify-end items-center">
								<Link
									href="/profile"
									className="text-gray-800 border-solid border-black rounded-xl p-1 border-2 hover:text-white hover:bg-black mx-2 sm:mx-4 capitalize tracking-wide transition-all"
								>
									Profile
								</Link>
								<Link
									onClick={handleLogout}
									href={"/"}
									className="text-white border-solid border-blue-600 rounded-xl p-1 border-2 bg-blue-600 hover:bg-blue-700 tracking-wide transition-all"
								>
									Logout
								</Link>
							</div>
						</>
					) : (
						<>
							<div className="col-start-10 col-end-12 font-medium flex justify-end items-center">
								<Link
									href="/auth/login/"
									className="text-gray-800 border-solid border-black rounded-xl p-1 border-2 hover:text-white hover:bg-black mx-2 sm:mx-4 capitalize tracking-wide transition-all"
								>
									Sign In
								</Link>
								<Link
									href={"/auth/register/"}
									className="text-white border-solid border-blue-600 rounded-xl p-1 border-2 bg-blue-600 hover:bg-blue-700 tracking-wide transition-all"
								>
									Sign Up
								</Link>
							</div>
						</>
					)
					}

				</nav>
			</header>
			{/* Mobile Navigation */}

			<nav className="bg-blue-300 bg-transparent-20 fixed lg:hidden bottom-0 left-0 right-0 z-20 px-4 sm:px-8 shadow-t ">
				<div className=" sm:px-3">
					<ul className="flex w-full justify-between items-center text-black-500">
						<Link
							href={"/"}
							className={
								"mx-1 sm:mx-2 px-3 sm:px-4 py-2 flex flex-col items-center text-xs border-t-2 transition-all "}
						>
							<svg
								className="w-6 h-6"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									strokeWidth={2}
									d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
							About
						</Link>

						<Link
							href={"/subscription"}
							className={
								"mx-1 sm:mx-2 px-3 sm:px-4 py-2 flex flex-col items-center text-xs border-t-2 transition-all "
							}
						>
							<svg
								className="w-6 h-6"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									strokeWidth={2}
									d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
							Subscription
						</Link>
						{isAuthenticated ? (
							<Link
							href={"/projects"}
							className={
								"mx-1 sm:mx-2 px-3 sm:px-4 py-2 flex flex-col items-center text-xs border-t-2 transition-all "
							}
						>
							<svg
								className="w-6 h-6"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									strokeWidth={2}
									d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
								/>
							</svg>
							Projects
						</Link>
						): null}
					</ul>
				</div>
			</nav>
			{/* End Mobile Navigation */}
		</>
	);
};
