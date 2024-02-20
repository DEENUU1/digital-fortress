'use client';
import React, {useState} from "react";
import {
	Button,
	Modal,
	ModalBody,
	ModalContent,
	ModalFooter,
	ModalHeader,
	Input,
	useDisclosure
} from "@nextui-org/react";
import {useRetrieveUserQuery} from '@/redux/features/authApiSlice';
import {toast} from 'react-toastify';


export default function UpdateProject({currentTitle, projectId}: {currentTitle: string, projectId: number}) {
	const {isOpen, onOpen, onOpenChange} = useDisclosure();
	const [isLoading, setIsLoading] = useState<boolean>(false);
	const [title, setTitle] = useState<string>(currentTitle);
	const {data: user} = useRetrieveUserQuery()

	const handleSubmit = async (e: any) => {
		e.preventDefault();

		setIsLoading(true);

		const data = JSON.stringify({
			"title": title,
			"user": user?.id,
		})

		try {
			const response = await fetch(process.env.API_URL + `api/v1/project/${projectId}/`, {
				method: "PUT",
				headers: {
					"Content-Type": "application/json"
				},
				credentials: "include",
				body: data
			})

			if (response.ok) {
				toast.success("Project updated successfully")
			} else {
				toast.error("Something went wrong. Please Try again.")
			}

		} catch (e) {
			toast.error("Something went wrong. Please Try again.");
		} finally {
			setIsLoading(false);
			onOpenChange();
		}
	}

	return (
		<>
			<Button size={"sm"} onPress={onOpen}><strong>Update</strong></Button>
			<Modal isOpen={isOpen} onOpenChange={onOpenChange} backdrop={"blur"}>
				<ModalContent>
					{(onClose) => (
						<>
							<ModalHeader className="flex flex-col gap-1">Update project</ModalHeader>
							<form onSubmit={handleSubmit}>
								<ModalBody>
									<Input
										label="Title"
										placeholder={currentTitle}
										onChange={(e) => setTitle(e.target.value)}
									/>
								</ModalBody>
								<ModalFooter>
									<Button color="danger" variant="light" onPress={onClose}>
										Close
									</Button>
									<Button color="warning" type="submit" isLoading={isLoading}>
										Update
									</Button>
								</ModalFooter>
							</form>
						</>
					)}
				</ModalContent>
			</Modal>
		</>
	);
}
