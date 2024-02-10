'use client'

import ProjectCard from "./ProjectCard"

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
	const projects: ProjectResponse[] = await getProjects();

	return (
		<section id="Projects"
						 className="w-fit mx-auto grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 justify-items-center justify-center gap-y-20 gap-x-14 mt-10 mb-5">

			{projects.length === 0 ? (
				<p>You don not have any saved offers</p>
			) : (
				projects.map((project: ProjectResponse) => (
					<ProjectCard key={project.id} title={project.title} id={project.id} created_at={project.created_at} />

				))
			)}
		</section>
	)
}