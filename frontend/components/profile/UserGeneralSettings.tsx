import React, {useState} from "react";
import {useRetrieveUserQuery} from "@/redux/features/authApiSlice";
import {Button} from "@nextui-org/react";
import {toast} from "react-toastify";


export default function UserGeneralSettings(){
	const {data: user} = useRetrieveUserQuery()
	const [isLoading, setIsLoading] = useState(false);
	const [apiKey, setApiKey] = useState<string>('');

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
    <div className="max-w-3xl mx-auto">
      <div className="mb-4">
        <label htmlFor="firstName" className="text-gray-600 block">First Name:</label>
        <input
          type="text"
          id="firstName"
          name="firstName"
          className="border border-gray-300 px-3 py-2 rounded focus:outline-none focus:ring focus:border-blue-500 w-full"
          placeholder={user?.first_name}
          disabled={true}
        />
      </div>
      <div className="mb-4">
        <label htmlFor="lastName" className="text-gray-600 block">Last Name:</label>
        <input
          type="text"
          id="lastName"
          name="lastName"
          className="border border-gray-300 px-3 py-2 rounded focus:outline-none focus:ring focus:border-blue-500 w-full"
          placeholder={user?.last_name}
          disabled={true}
        />
      </div>
      <div className="mb-4">
        <label htmlFor="email" className="text-gray-600 block">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          className="border border-gray-300 px-3 py-2 rounded focus:outline-none focus:ring focus:border-blue-500 w-full"
          placeholder={user?.email}
          disabled={true}
        />
      </div>
      <form onSubmit={handleSubmit} className="mb-4">
        <label htmlFor="apiKey" className="text-gray-600 block">API Key:</label>
        <input
          onChange={(e) => setApiKey(e.target.value)}
          type="text"
          id="apiKey"
          name="apiKey"
          className="border border-gray-300 px-3 py-2 rounded focus:outline-none focus:ring focus:border-blue-500 w-full"
          placeholder={user?.openai_key}
        />
        <Button type="submit" color="success" isLoading={isLoading} className="mt-4">
          {isLoading ? "Loading..." : "Save"}
        </Button>
      </form>
    </div>
  );
}