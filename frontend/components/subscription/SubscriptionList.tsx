'use client'
import {SubscriptionCard} from "./SubscriptionCard";

export async function getSubscriptions() {
	const response = await fetch(process.env.API_URL + "api/v1/subscription", {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
		cache: "no-store"
	});
	return response.json();
}


export default async function SubscriptionList() {
	const subscriptions: SubscriptionResponse[] = await getSubscriptions();

	return (
		<section>
			<div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
				<div className="mx-auto max-w-screen-md text-center mb-8 lg:mb-12">
					<h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Subscription options</h2>
				</div>
				<div className="space-y-8 lg:grid lg:grid-cols-3 sm:gap-6 xl:gap-10 lg:space-y-0">
					{subscriptions.length === 0 ? (
						<p>No subscriptions are available now</p>
					): (
						subscriptions.map((subscription: SubscriptionResponse) => (
							<SubscriptionCard key={subscription.id} data={subscription}/>
						))
					)}
				</div>
			</div>

		</section>
	)
}