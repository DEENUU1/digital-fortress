'use client';
import React, {useState} from "react";
import {
	Button,
	Modal,
	ModalBody,
	ModalContent,
	ModalFooter,
	ModalHeader,
	Textarea,
	useDisclosure
} from "@nextui-org/react";
import {useRetrieveUserQuery} from '@/redux/features/authApiSlice';
import {toast} from 'react-toastify';


export default function ModalCreateScenario({parent_id, project_id}: { parent_id: number | null, project_id: number }) {
	const {isOpen, onOpen, onOpenChange} = useDisclosure();
	const [isLoading, setIsLoading] = useState<boolean>(false);
	const [useDetails, setUserDetails] = useState<string | null>();
	const {data: user} = useRetrieveUserQuery()

	const handleSubmit = async (e: any) => {
		e.preventDefault();

		setIsLoading(true);

		const data = JSON.stringify({
			"parent_id": parent_id,
			"project": project_id,
			"user_details": useDetails,
			"user": user?.id,
		})

		try {
			const response = await fetch(process.env.API_URL + "api/v1/scenario/", {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				credentials: "include",
				body: data
			})

			if (response.ok) {
				toast.success("Scenario created successfully")
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
			<Button size="sm" color="success" onPress={onOpen}>Create</Button>
			<Modal isOpen={isOpen} onOpenChange={onOpenChange} backdrop={"blur"}>
				<ModalContent>
					{(onClose) => (
						<>
							<ModalHeader className="flex flex-col gap-1">Create scenario</ModalHeader>
							<form onSubmit={handleSubmit}>
								<ModalBody>
									<Textarea
										label="Details"
										placeholder="Enter more informations"
										onChange={(e) => setUserDetails(e.target.value)}
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
