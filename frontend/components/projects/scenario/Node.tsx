'use client';
import React from "react";
import ModalResponse from "@/components/projects/scenario/ModalResponse";
import ModalCreateScenario from "@/components/projects/scenario/ModalCreateScenario";


export default function Node({data}: { data: ScenarioResponse }) {

	return (
		<div className="p-3 ml-auto mr-auto bg-blue-300 bg-opacity-40 rounded-xl shadow-inner">
			<div>
				{data.response ? <p className="text-sm"><strong>AI: </strong>{data.response}</p> : null}
				{data.user_details ? <p className="text-sm"><strong>User: </strong>{data.user_details}</p> : null}
			</div>

			<div className="space-x-2 mt-5">
				<ModalResponse data={data}></ModalResponse>
				<ModalCreateScenario parent_id={data.id} project_id={data.project}></ModalCreateScenario>
			</div>
		</div>
	);
}