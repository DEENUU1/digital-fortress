'use client';

import {Tree, TreeNode} from 'react-organizational-chart';
import Node from "@/components/projects/scenario/Node";
import getTree from "@/components/projects/scenario/getTree";
import constructTree from "@/components/projects/scenario/constructTree";
import ModalCreateScenario from "@/components/projects/scenario/ModalCreateScenario";
import ProjectDetailsModal from "@/components/projects/ProjectDetails";
import FileList from "@/components/projects/FileList";
import {useState, useEffect} from "react";
import {Simulate} from "react-dom/test-utils";
import compositionUpdate = Simulate.compositionUpdate;

interface PageParams {
	id: number;
}


export default function Page({params}: { params: PageParams }) {
	// const treeData: ScenarioResponse[] = getTree(params.id);
	const [treeData, setTreeData] = useState<ScenarioResponse[]>([]);
	
	const fetchTreeData = () => {
    fetch(process.env.API_URL + `api/v1/scenario/tree/${params.id}`, {
      credentials: "include"
    })
      .then(response => response.json())
      .then(data => setTreeData(data));
	}

	useEffect(() => {
		fetchTreeData()
	}, []);

	const handleOnUpdateTree = () => {
  	fetchTreeData();
		const tree = constructTree(treeData);
		renderTreeNodes(tree);
	}
	const tree = constructTree(treeData);

	const renderTreeNodes = (nodes: ScenarioResponse[] | undefined) => {
		if (!nodes) return null;
		return nodes.map(node => (
			<TreeNode key={node.id} label={<Node data={node} onUpdateTree={handleOnUpdateTree}></Node>}>
				{renderTreeNodes(node.children)}
			</TreeNode>
		));
	};

	if (treeData.length <= 0) {
		return (
			<main>
				<div className="space-x-2 p-4">
					<ProjectDetailsModal projectId={params.id}/>
					<FileList projectId={params.id}/>
					<ModalCreateScenario parent_id={null} project_id={params.id} onUpdateTree={handleOnUpdateTree}/>
				</div>
				<section className="h-screen flex items-center justify-center">
					<h1 className="text-2xl font-bold">Click &apos;create&apos; to start your scenario.</h1>
				</section>
			</main>
		)
	} else {
		return (
			<main>
				<div className="space-x-2 p-4">
					<ProjectDetailsModal projectId={params.id}/>
					<FileList projectId={params.id}/>
				</div>
				<Tree label={<div>Root</div>}>
					{renderTreeNodes(tree)}
				</Tree>
			</main>
		);
	}
}