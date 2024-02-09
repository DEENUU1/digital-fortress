'use client';
import React from "react";
import ModalResponse from "@/components/projects/scenario/ModalResponse";
import ModalCreateScenario from "@/components/projects/scenario/ModalCreateScenario";


export default function Node({data}: { data: ScenarioResponse }) {

	return (
		<div>
			<strong>{data.id}</strong>
			<ModalResponse data={data}></ModalResponse>
			<ModalCreateScenario parent_id={data.id} project_id={data.project}></ModalCreateScenario>
		</div>
	);
}