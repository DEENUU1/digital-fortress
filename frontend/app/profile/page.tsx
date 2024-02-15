'use client'
import React, {useState} from "react";
// import {Metadata} from "next";
import {useRetrieveUserQuery} from "@/redux/features/authApiSlice";
import {Button, Input} from "@nextui-org/react";
import {EyeFilledIcon} from "@/components/profile/EyeFilledIcon";
import {EyeSlashFilledIcon} from "@/components/profile/EyeSlashFilledIcon";
import {toast} from "react-toastify";

// export const metadata: Metadata = {
// 	title: 'Digital Fortress | Profile',
// }


export default function Page() {
	const [isVisible, setIsVisible] = useState<boolean>(false);
	const [apiKey, setApiKey] = useState<string>('');
	const [isLoading, setIsLoading] = useState(false);
	const {data: user} = useRetrieveUserQuery()

	const toggleVisibility = () => setIsVisible(!isVisible);
	const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();

		setIsLoading(true);

		const data = JSON.stringify({
			"openai_key": apiKey,
		})

		try {
			const response = await fetch(process.env.API_URL + "api/v1/user/me/api_key/", {
				method: "PUT",
				headers: {
					"Content-Type": "application/json"
				},
				credentials: "include",
				body: data
			})

			if (response.ok) {
				toast.success("OpenAI key updated successfully")
			} else {
				toast.error("Something went wrong. Please Try again.")
			}

		} catch (e) {
			toast.error("Something went wrong. Please Try again.");
		} finally {
			setIsLoading(false);
		}
	}


	return (
		<>
			<main className="flex min-h-screen flex-col items-center justify-between p-24">
				<form onSubmit={handleSubmit}>
					<div className="grid grid-cols-2 gap-4">
						<Input isDisabled type="text" label="First name" placeholder={user?.first_name}/>
						<Input isDisabled type="text" label="Last name" placeholder={user?.last_name}/>
					</div>
					<div className="grid grid-cols-2 gap-4">
						<Input
							value={apiKey}
							onChange={(e) => setApiKey(e.target.value)}
							defaultValue={apiKey}
							label="OpenAI API KEY"
							variant="bordered"
							placeholder="Enter your OpenAI API KEY"
							endContent={
								<button className="focus:outline-none" type="button" onClick={toggleVisibility}>
									{isVisible ? (
										<EyeSlashFilledIcon className="text-2xl text-default-400 pointer-events-none"/>
									) : (
										<EyeFilledIcon className="text-2xl text-default-400 pointer-events-none"/>
									)}
								</button>
							}
							type={isVisible ? "text" : "password"}
						/>
						<Button type={"submit"} color="success" isLoading={isLoading}>
							{isLoading ? "Loading..." : "Save"}
						</Button>
					</div>
				</form>
			</main>
		</>
	)
}

