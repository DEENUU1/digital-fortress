'use client'
import React from "react";
import UserGeneralSettings from "@/components/profile/UserGeneralSettings";

export default function Page() {

	return (
		<>
			<main className="flex min-h-screen flex-col items-center justify-between p-24">
				<div>
					<h1 className="text-center font-bold text-3xl mb-5">Settings</h1>
					<UserGeneralSettings/>
				</div>
			</main>
		</>
	)
}

