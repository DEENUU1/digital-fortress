'use client'

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
		<section id="Projects"
						 className="w-fit mx-auto grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 justify-items-center justify-center gap-y-20 gap-x-14 mt-10 mb-5">

			{subscriptions.length === 0 ? (
				<p>You don not have any saved offers</p>
			) : (
				subscriptions.map((subscription: SubscriptionResponse) => (
					<div key={subscription.id} >{subscription.description}</div>
				))
			)}
		</section>
	)
}