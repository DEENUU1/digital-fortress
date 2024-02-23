import DeleteProjectButton from "@/components/projects/DeleteProject";
import UpdateProject from "@/components/projects/UpdateProject";

export default function ProjectCard(
	{
		title,
		id,
		onDeleteProjects,
	}: {
		title: string,
		id: number,
		created_at: string,
		onDeleteProjects: () => void
	}
) {


	return (
		<div className="w-72 bg-white shadow-md rounded-xl duration-500 hover:scale-105 hover:shadow-xl">
			<a href={`/projects/${id}`}>
				<div className="px-4 py-3 w-72">
					<p className="text-lg font-bold text-black truncate block capitalize">{title}</p>
				</div>
			</a>
			<div className="space-x-2 p-4">
				<DeleteProjectButton projectId={id} onDeleteProjects={onDeleteProjects}/>
				<UpdateProject currentTitle={title} projectId={id} onUpdateProject={onDeleteProjects}/>
			</div>
		</div>
	)
}