'use client'

export async function getProjects() {
	const response = await fetch(process.env.API_URL + "api/v1/project", {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
		credentials: 'include',
		cache: "no-store"
	});
	return response.json();
}


export default async function ProjectList() {
	const projects = await getProjects();

	return (
		<div>
			{projects.length === 0 ? (
				<p>You don not have any saved offers</p>
			) : (
				projects.map((project: ProjectResponse) => (
					<div key={project.id}><h1>{project.title}</h1></div>
				))
			)}
		</div>
	)
}