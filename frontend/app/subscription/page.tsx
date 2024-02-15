import React, {Suspense} from "react";
import Spinner from "@/components/common/Spinner";
import {Metadata} from "next";
import SubscriptionList from "@/components/subscription/SubscriptionList";

export const metadata: Metadata = {
	title: 'Digital Fortress | Subscription Plans',
}

export default async function Page() {
	return (
		<>
			<main className="flex min-h-screen flex-col items-center justify-between p-24">

				<div>
					<h1 className="text-center font-bold text-3xl mb-5">Subscriptions</h1>
					<Suspense fallback={<Spinner/>}>
						<SubscriptionList/>
					</Suspense>

				</div>
			</main>
		</>
	)
}
