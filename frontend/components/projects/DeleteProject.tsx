'use client'
import {toast} from "react-toastify";
import {useState} from "react";
import {Button} from "@nextui-org/react";

export default function DeleteProjectButton({projectId}: { projectId: number }) {
	const [isLoading, setIsLoading] = useState<boolean>(false);

	const handleDelete = async () => {
		setIsLoading(true);

		try {
			const response = await fetch(process.env.API_URL + `api/v1/project/${projectId}`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json',
				},
				credentials: 'include',
			});

			if (response.ok) {
				toast.success("Project deleted.")
			}
			else {
				toast.error("Can't delete project.")
			}
		} catch {
			toast.error("Error. Please try again.")
		} finally {
			setIsLoading(false)
		}
	}

	return (
		<>
      <Button size={"sm"} color="danger" onClick={handleDelete} isLoading={isLoading}><strong>Delete</strong></Button>
		</>
	)
}