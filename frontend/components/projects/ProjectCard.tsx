import DeleteProjectButton from "@/components/projects/DeleteProject";
import UpdateProject from "@/components/projects/UpdateProject";

export default function ProjectCard(
	{
		title,
		id,
		created_at
	}: {
		title: string,
		id: number,
		created_at: string,
	}
) {


	return (
		<div className="w-72 bg-white shadow-md rounded-xl duration-500 hover:scale-105 hover:shadow-xl">
			<a href={`/projects/${id}`}>
				<div className="px-4 py-3 w-72">
					<p className="text-lg font-bold text-black truncate block capitalize">{title}</p>
					<div className="flex items-center">
						<p className="text-sm font-semibold text-black cursor-auto my-3">{created_at}</p>
					</div>
				</div>
			</a>
			<DeleteProjectButton projectId={id} />
			<UpdateProject currentTitle={title} projectId={id} />
		</div>
	)
}