'use client';

import { store } from './store';
import { Provider } from 'react-redux';
import {NextUIProvider} from '@nextui-org/react'

interface Props {
	children: React.ReactNode;
}

export default function CustomProvider({ children }: Props) {
	return (
		<NextUIProvider>
			<Provider store={store}>{children}</Provider>
		</NextUIProvider>
	)
}
