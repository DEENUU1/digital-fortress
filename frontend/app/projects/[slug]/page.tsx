'use client';

import React, {useEffect, useState} from "react";
import {Tree, TreeNode} from 'react-organizational-chart';
import Node from "@/components/projects/scenario/Node";

interface PageParams {
	slug: string;
}



export function getTree(projectSlug: string) {
	// eslint-disable-next-line react-hooks/rules-of-hooks
	const [tree, setTree] = useState<ScenarioResponse[]>([]);

	// eslint-disable-next-line react-hooks/rules-of-hooks
	useEffect(() => {
		fetch(process.env.API_URL + `api/v1/scenario/tree/${projectSlug}`, {
			credentials: "include"
		})
			.then(response => response.json())
			.then(data => setTree(data));
	}, [projectSlug]);

	return tree
}

function constructTree(data: ScenarioResponse[]) {
	const map = new Map<number, ScenarioResponse>();
	const rootNodes: ScenarioResponse[] = [];

	data.forEach(node => {
		map.set(node.id, node);
		node.children = [];
	});

	data.forEach(node => {
		const parent = map.get(node.parent_id || 0);
		if (parent) {
			parent.children.push(node);
		} else {
			rootNodes.push(node);
		}
	});

	return rootNodes;
}


export default function Page({params}: { params: PageParams }) {
	const treeData: ScenarioResponse[] = getTree(params.slug);
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
		return <div>Create root tree</div>
	} else {
		return (
			<main>
				<Tree label={<div>Root</div>}>
					{renderTreeNodes(tree)}
				</Tree>
			</main>
		);
	}


}