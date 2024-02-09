'use client';

import React from "react";
import {Tree, TreeNode} from 'react-organizational-chart';
import Node from "@/components/projects/scenario/Node";
import getTree from "@/components/projects/scenario/getTree";
import constructTree from "@/components/projects/scenario/constructTree";

interface PageParams {
	slug: string;
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