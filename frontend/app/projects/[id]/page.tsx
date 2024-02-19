'use client';

import React from "react";
import {Tree, TreeNode} from 'react-organizational-chart';
import Node from "@/components/projects/scenario/Node";
import getTree from "@/components/projects/scenario/getTree";
import constructTree from "@/components/projects/scenario/constructTree";
import ModalCreateScenario from "@/components/projects/scenario/ModalCreateScenario";
import ProjectDetailsModal from "@/components/projects/ProjectDetails";
import FileList from "@/components/projects/FileList";


interface PageParams {
	id: number;
}


export default function Page({params}: { params: PageParams }) {
	const treeData: ScenarioResponse[] = getTree(params.id);
	const tree = constructTree(treeData);

	const renderTreeNodes = (nodes: ScenarioResponse[] | undefined) => {
		if (!nodes) return null;
		return nodes.map(node => (
			<TreeNode key={node.id} label={<Node data={node}></Node>}>
				{renderTreeNodes(node.children)}
			</TreeNode>
		));
	};

	if (treeData.length <= 0) {
		return (
			<main>
				<ProjectDetailsModal projectId={params.id}/>
				<h2>Create root tree</h2>
				<ModalCreateScenario parent_id={null} project_id={params.id}></ModalCreateScenario>
				<FileList projectId={params.id}></FileList>
			</main>
		)
	} else {
		return (
			<main>
				<ProjectDetailsModal projectId={params.id}/>
				<FileList projectId={params.id}></FileList>
				<Tree label={<div>Root</div>}>
					{renderTreeNodes(tree)}
				</Tree>
			</main>
		);
	}
}