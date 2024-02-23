
export function SubscriptionCard({data}: { data: SubscriptionResponse }) {
	const firstPrice = data.price[0];

	return (
		<>
			<div
				className={`flex flex-col p-6 mx-auto max-w-lg text-center text-gray-900 bg-white rounded-lg border ${
					firstPrice.value === "0.00" ? 'border-green-600 border-3' : 'border-gray-100'
				} shadow dark:border-gray-600 xl:p-8 dark:bg-gray-800 dark:text-white hover:scale-105 hover:shadow-xl`}
			>
				<div className="flex justify-center items-baseline my-8">
					<h1><strong className="text-4xl">{firstPrice.value}</strong> {firstPrice.currency}</h1>
				</div>
				<h3 className="mb-4 text-2xl font-semibold">{data.name}</h3>
				<p className="font-light text-gray-500 sm:text-lg dark:text-gray-400 mb-3">{data.description}</p>
				<ul role="list" className="mb-8 space-y-4 text-left">
					<li className="flex items-center space-x-3">
						<svg className="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor"
								 viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd"
										d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
										clip-rule="evenodd"></path>
						</svg>
						<span>Max storage per project <strong>{data.max_project_storage}</strong></span>
					</li>
					<li className="flex items-center space-x-3">
						<svg className="flex-shrink-0 w-5 h-5 text-green-500 dark:text-green-400" fill="currentColor"
								 viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
							<path fill-rule="evenodd"
										d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
										clip-rule="evenodd"></path>
						</svg>
						<span>Number of active <strong>projects {data.num_of_projects}</strong></span>
					</li>
				</ul>
				<a href="#"
					 className="text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:text-white  dark:focus:ring-primary-900">Get
					started</a>
			</div>
		</>

	)
}

