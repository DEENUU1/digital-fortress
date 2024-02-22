'use client';

import ProjectList from "@/components/projects/ProjectList";
import React, {Suspense, useEffect, useState} from "react";
import CreateProject from "@/components/projects/CreateProject";

export default function Page() {
	const [projects, setProjects] = useState<ProjectResponse[]>([]);

	const handleFetchProjects = () => {
			fetch(process.env.API_URL + "api/v1/project", {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
			},
			credentials: 'include',
		})
			.then(response => response.json())
			.then(data => setProjects(data));
	}

	useEffect(() => {
		handleFetchProjects()
	}, []);

	return (
		<>
			<main className="flex min-h-screen flex-col items-center justify-between p-24">

				<div>
					<h1 className="text-center font-bold text-3xl mb-5">Your projects</h1>
					<CreateProject onUpdateProjects={handleFetchProjects}/>
					<ProjectList projects={projects} onDeleteProjects={handleFetchProjects}/>
				</div>
			</main>
		</>
	)
}
