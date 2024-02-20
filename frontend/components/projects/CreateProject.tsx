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


export default function CreateProject() {
	const {isOpen, onOpen, onOpenChange} = useDisclosure();
	const [isLoading, setIsLoading] = useState<boolean>(false);
	const [title, setTitle] = useState<string>();
	const {data: user} = useRetrieveUserQuery()

	const handleSubmit = async (e: any) => {
		e.preventDefault();

		setIsLoading(true);

		const data = JSON.stringify({
			"title": title,
			"user": user?.id,
		})

		try {
			const response = await fetch(process.env.API_URL + "api/v1/project/", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				credentials: "include",
				body: data
			})

			if (response.ok) {
				toast.success("Project created successfully")
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
			<Button color={"success"} onPress={onOpen}><strong>Create</strong></Button>
			<Modal isOpen={isOpen} onOpenChange={onOpenChange} backdrop={"blur"}>
				<ModalContent>
					{(onClose) => (
						<>
							<ModalHeader className="flex flex-col gap-1">Create project</ModalHeader>
							<form onSubmit={handleSubmit}>
								<ModalBody>
									<Input
										label="Title"
										placeholder="Title of a project"
										onChange={(e) => setTitle(e.target.value)}
									/>
								</ModalBody>
								<ModalFooter>
									<Button color="danger" variant="light" onPress={onClose}>
										Close
									</Button>
									<Button color="success" type="submit" isLoading={isLoading}>
										Create
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
