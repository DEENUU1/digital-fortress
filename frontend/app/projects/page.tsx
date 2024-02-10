import ProjectList from "@/components/projects/ProjectList";
import React, {Suspense} from "react";
import Spinner from "@/components/common/Spinner";
import {Metadata} from "next";
import CreateProject from "@/components/projects/CreateProject";

export const metadata: Metadata = {
	title: 'Digital Fortress | Projects',
}

export default async function Page() {
	return (
		<>
			<main className="flex min-h-screen flex-col items-center justify-between p-24">

				<div>
					<h1 className="text-center font-bold text-3xl mb-5">Your projects</h1>
					<CreateProject/>
					<Suspense fallback={<Spinner/>}>
						<ProjectList/>
					</Suspense>

				</div>
			</main>
		</>
	)
}
