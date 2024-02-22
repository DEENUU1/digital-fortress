import React, { useState, useEffect } from 'react';
import ProjectCard from "./ProjectCard"

export default function ProjectList({projects, onDeleteProjects}: {projects: ProjectResponse[], onDeleteProjects: () => void}) {
	return (
		<section id="Projects"
						 className="w-fit mx-auto grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 justify-items-center justify-center gap-y-20 gap-x-14 mt-10 mb-5">

			{projects.length === 0 ? (
				<p>You don not have any saved offers</p>
			) : (
				projects.map((project: ProjectResponse) => (
					<ProjectCard key={project.id} title={project.title} id={project.id} created_at={project.created_at} onDeleteProjects={onDeleteProjects} />
				))
			)}
		</section>
	)
}