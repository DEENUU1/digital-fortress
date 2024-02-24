import React from "react";


export default function Input(
	{
		placeholderValue,
		type,
		id,
		name
	}:
		{
			placeholderValue: string | undefined,
			type: string,
			id: string,
			name: string
		}
) {

	return (
		<input
			type={type}
			id={id}
			name={name}
			className="border border-gray-300 px-3 py-2 rounded focus:outline-none focus:ring focus:border-blue-500 w-full"
			placeholder={placeholderValue ? placeholderValue : ""}
			disabled={true}
		/>
	)
}