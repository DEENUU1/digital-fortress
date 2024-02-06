import { apiSlice } from '../services/apiSlice';

interface User {
	first_name: string;
	last_name: string;
	email: string;
	id: number;
}

const authApiSlice = apiSlice.injectEndpoints({
	endpoints: builder => ({
		retrieveUser: builder.query<User, void>({
			query: () => '/user/me/',
		}),
		login: builder.mutation({
			query: ({ email, password }) => ({
				url: '/user/token/login/',
				method: 'POST',
				body: { email, password },
			}),
		}),
		register: builder.mutation({
			query: ({
				first_name,
				last_name,
				email,
				password,
				re_password,
				account_type,
			}) => ({
				url: '/user/register/',
				method: 'POST',
				body: { first_name, last_name, email, password, re_password, account_type},
			}),
		}),
		verify: builder.mutation({
			query: () => ({
				url: '/user/token/verify/',
				method: 'POST',
			}),
		}),
		logout: builder.mutation({
			query: () => ({
				url: '/user/token/verify/',
				method: 'POST',
			}),
		}),
	}),
});

export const {
	useRetrieveUserQuery,
	useLoginMutation,
	useRegisterMutation,
	useVerifyMutation,
	useLogoutMutation,
} = authApiSlice;
