import {toast} from "react-toastify";
import {useState} from "react";
import {useRetrieveUserQuery} from "@/redux/features/authApiSlice";
import {Button} from "@nextui-org/react";

export default function FileUpload({projectId}: {projectId: number}){
	const [file, setFile] = useState(null);
	const [isLoading, setIsLoading] = useState(false);
	const {data: user} = useRetrieveUserQuery()

	const handleFileUpload = async (e: any) => {
		e.preventDefault();

		setIsLoading(true);

		const formData = new FormData();
		// @ts-ignore
		formData.append("user", user?.id);
		formData.append("project", projectId.toString());
		if (file !== null && typeof file !== "string") {
			formData.append("file", file);
		}

		try {
			const response = await fetch(process.env.API_URL + "/api/v1/file/", {
				method: "POST",
				credentials: "include",
				body: formData
			})

			if (response.ok) {
				toast.success("File uploaded successfully");
			} else {
				toast.error("Can't upload file");
			}

		} catch (error) {
			toast.error("Error uploading file");
		} finally {
			setIsLoading(false);
		}
	}

	const handleSetFile = (e: any) => {
		setFile(e.target.file[0])
	}

	return (
		<>
			<form onSubmit={handleFileUpload}>
				<input
					className="border text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 border-gray-600 placeholder-gray-400"
					id="logo"
					type="file"
					onChange={(e) => handleSetFile(e)}
				/>
				<Button isLoading={isLoading} type="submit">{isLoading ? "Uploading..." : "Upload"}</Button>
			</form>
		</>
	)
}